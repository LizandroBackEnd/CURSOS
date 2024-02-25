import Image from 'next/image'
import CarouselClient from './component/CarouselClient'


export default function Home() {
  return (
    <div className="container-fluid  pt-5 ">
      <CarouselClient/>
    </div>
  )
}